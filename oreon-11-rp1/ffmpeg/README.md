# FFMPEG

FFmpeg is a multimedia framework, able to decode, encode, transcode, mux,
demux, stream, filter and play pretty much anything that humans and machines
have created. It supports the most obscure ancient formats up to the cutting
edge. No matter if they were designed by some standards committee, the
community or a corporation.

## How to bump ABI

1. `fedpkg request-side-tag`
2. `koji edit-sidetag --rpm-macro=_with_bootstrap=1 fxx-build-side-yyyyyy`
3. bootstrap `ffmpeg`
4. bootstrap `libheif`
5. bootstrap `vtk`
6. build `chromaprint`
7. `koji edit-sidetag --remove-rpm-macro=_with_bootstrap fxx-build-side-yyyyyy`
5. unbootstrap `vtk`
6. unbootstrap `ffmpeg`
7. unbootstrap `libheif`
8. continue with other dependents (`fedrq wrsrc -s ffmpeg -F name`)

### Rebuild priority:

* `cef`
* `opencv`
* `kf6-kfilemetadata`
* `qt6-qtmultimedia`
* `qt6-qtwebengine`
