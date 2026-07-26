%global source0_hash 10e473801143b45a60b2678772391d3ddc8c5a15e41fe0ee227368fb79a2c920

%global debug_package %{nil}

Name:           reStream
Version:        1.4.0
Release:        %autorelease
URL:            https://github.com/rien/reStream
Summary:        Stream your reMarkable screen over SSH
License:        MIT
BuildArch:      noarch

Source:         %{url}/archive/v%{version}/reStream-v%{version}.tar.gz

BuildRequires:  help2man

Requires:       /usr/bin/sh
Requires:       openssh-clients
Requires:       (ffmpeg-free >= 4.0.0 or ffmpeg >= 4.0.0)
Requires:       lz4

%description
Stream your reMarkable screen over SSH.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
# Fix command name in manpage
ln -s reStream.sh reStream
help2man -N ./reStream -o reStream.1
sed -i 's/\.\///g' reStream.1
rm -f reStream

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 reStream.sh %{buildroot}%{_bindir}/reStream
mkdir -p %{buildroot}%{_mandir}/man1/
install -pm 0644 reStream.1 %{buildroot}%{_mandir}/man1/reStream.1

%files
%license LICENSE
%doc README.md
%{_bindir}/reStream
%{_mandir}/man1/reStream.1*

%changelog
%autochangelog
