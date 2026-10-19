%global source0_hash 0f76218e9b64f8398e7686065204cd1d201f0442dfdab77fbbc3b2f0fcd1566b
%global debug_package %{nil}
Name:           reStream
Version:        1.5.0
Release:        1%{?dist}
URL:            https://github.com/rien/reStream
Summary:        Stream your reMarkable screen over SSH
License:        MIT
BuildArch:      noarch
Source0:        https://github.com/rien/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz
Requires:       /usr/bin/sh
Requires:       openssh-clients
Requires:       (ffmpeg-free >= 4.0.0 or ffmpeg >= 4.0.0)
Requires:       lz4
# oreon:deps
BuildRequires:  help2man
# /oreon:deps
%description
Stream your reMarkable screen over SSH.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

ln -s reStream.sh reStream
help2man -N ./reStream -o reStream.1
sed -i 's/\.\///g' reStream.1
rm -f reStream
%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 reStream.sh %{buildroot}%{_bindir}/reStream
mkdir -p %{buildroot}%{_mandir}/man1/
install -pm 0644 reStream.1 %{buildroot}%{_mandir}/man1/reStream.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
