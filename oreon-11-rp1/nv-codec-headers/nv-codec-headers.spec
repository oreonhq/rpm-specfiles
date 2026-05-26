Name:           nv-codec-headers
Version:        13.0.19.0
Release:        3%{?dist}
Summary:        FFmpeg version of Nvidia Codec SDK headers
License:        MIT
URL:            https://github.com/FFmpeg/nv-codec-headers
Source0:        https://github.com/FFmpeg/nv-codec-headers/archive/n13.0.19.0/nv-codec-headers-n13.0.19.0.tar.gz
# oreon url source checksums begin
%global source0_sha256 86d15d1a7c0ac73a0eafdfc57bebfeba7da8264595bf531cf4d8db1c22940116
%global source0_file nv-codec-headers-n13.0.19.0.tar.gz
# oreon url source checksums end

BuildArch:      noarch

BuildRequires:  make

%description
FFmpeg version of headers required to interface with Nvidias codec APIs.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/nv-codec-headers-n13.0.19.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "86d15d1a7c0ac73a0eafdfc57bebfeba7da8264595bf531cf4d8db1c22940116" || { echo "oreon: Source0 SHA256 mismatch for nv-codec-headers-n13.0.19.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n %{name}-n%{version}
sed -i -e 's@/include@/include/ffnvcodec@g' ffnvcodec.pc.in

# Extract license
sed -n '4,25p' include/ffnvcodec/nvEncodeAPI.h > LICENSE
sed -i '1,22s/^.\{,3\}//' LICENSE

%build
%make_build PREFIX=%{_prefix} LIBDIR=/share


%install
%make_install PREFIX=%{_prefix} LIBDIR=/share


%files
%doc README
%license LICENSE
%{_includedir}/ffnvcodec/
%{_datadir}/pkgconfig/ffnvcodec.pc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 13.0.19.0-3
- Prepare for Oreon 11 (RP1)
