from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import StreamType
from pytgcalls.exceptions import AlreadyJoinedError
from pytgcalls.types.input_stream import InputAudioStream, InputStream
from pelerbot.utils.basic import *
from pelerbot import *
from pelerbot.plugins.help import *



@Client.on_message(filters.me & filters.command("joinvc", COMMAND_HANDLER))
async def gbanuser(client: Client, message: Message):
    Msg = await message.edit_text("`Processing..`")
    if len(client.text.split()) > 1:
        chat_id = client.text.split()[1]
        try:
            chat_id = await client.get_peer_id(int(chat_id))
        except Exception as e:
            return await Msg.edit(f"**ERROR:** `{e}`")
    else:
        chat_id = client.chat_id
    file = "./pelerbot/utils/resources/audio-man.mp3"
    if chat_id:
        try:
            await call_py.join_group_call(
                chat_id,
                InputStream(
                    InputAudioStream(
                        file,
                    ),
                ),
                stream_type=StreamType().local_stream,
            )
            await Msg.edit(
                f"✪ **Berhasil Join Ke Obrolan Suara**\n└ **Chat ID:** `{chat_id}`"
            )
        except AlreadyJoinedError:
            await call_py.leave_group_call(chat_id)
            await Msg.edit(
                Man,
                "**ERROR:** `Karena akun sedang berada di obrolan suara`\n\n• Silahkan coba `.joinvc` lagi",
                45,
            )
        except Exception as e:
            await Msg.edit(f"**INFO:** `{e}`")
