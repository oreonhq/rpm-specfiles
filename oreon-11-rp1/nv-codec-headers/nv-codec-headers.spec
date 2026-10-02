%global source0_hash 2255bc74d038b95aa4be30f5f66322c2176acbdb90ada1851db6993536fbeaf7

Name:           nv-codec-headers
Version:        13.1.15.0
Release:        1%{?dist}
Summary:        FFmpeg version of Nvidia Codec SDK headers
License:        MIT
URL:            https://github.com/FFmpeg/nv-codec-headers
Source0:        https://github.com/FFmpeg/nv-codec-headers/archive/refs/tags/n%{version}.tar.gz#/%{name}-n%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make

%description
FFmpeg version of headers required to interface with Nvidias codec APIs.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
