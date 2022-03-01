import click
from azblobregex.core import get_match_blobs, download_blobs, delete_blobs
from azure.storage.blob import BlobServiceClient, ContainerClient

@click.group()
@click.option('--dry', default=False, is_flag=True)
@click.option("--st_connect_str", required=True, type=str)
@click.option("--blob_container", required=True, type=str)
@click.option("--filter_pattern", type=str, default=".*")
@click.pass_context
def cli(ctx, dry, st_connect_str, blob_container, filter_pattern):
    ctx.ensure_object(dict)
    ctx.obj['DRY'] = dry
    ctx.obj['ST_CONNECT_STR'] = st_connect_str
    ctx.obj['BLOB_CONTAINER'] = blob_container
    ctx.obj['FILTER_PATTERN'] = filter_pattern


@cli.command()
@click.pass_context
@click.option("--dl_target_dir", type=str, default="./download")
def download(ctx, dl_target_dir):
    click.echo('start download')

    blob_service_client = BlobServiceClient.from_connection_string(ctx.obj['ST_CONNECT_STR'])
    container_client: ContainerClient = blob_service_client.get_container_client(ctx.obj['BLOB_CONTAINER'])
    items = get_match_blobs(
        container_client=container_client,
        filter_pattern=ctx.obj['FILTER_PATTERN'],
                    )
    print(str(len(items)) + " items matched")

    if not ctx.obj['DRY'] :
        download_blobs(container_client=container_client,
                 items=items,
                 dl_target_dir=dl_target_dir)

    print("complete!")


@cli.command()
@click.pass_context
def delete(ctx):
    click.echo('start delete')

    blob_service_client = BlobServiceClient.from_connection_string(ctx.obj['ST_CONNECT_STR'])
    container_client: ContainerClient = blob_service_client.get_container_client(ctx.obj['BLOB_CONTAINER'])
    items = get_match_blobs(
        container_client=container_client,
        filter_pattern=ctx.obj['FILTER_PATTERN'],
    )
    print(str(len(items)) + " items matched")

    if not ctx.obj['DRY'] :
        delete_blobs(container_client=container_client, items=items)

    print("complete!")


if __name__ == '__main__':
    cli(obj={})
