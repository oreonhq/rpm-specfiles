%global source0_hash e91135281cb66569f2ca4c0bac277246991e7e52524c0ca8cba3de5c8e81cec9

Name:           ncdu
Version:        2.9.2
Release:        2%{?dist}
Summary:        Text-based disk usage viewer

License:        MIT
URL:            https://dev.yorhel.nl/ncdu/
Source0:        https://dev.yorhel.nl/download/ncdu-%{version}.tar.gz
Source1:        https://dev.yorhel.nl/download/ncdu-%{version}.tar.gz.asc
Source2:        https://yorhel.nl/key.asc

Patch0:         ncdu-allow-shlib-undefined.patch

ExclusiveArch:  %{zig_arches}

BuildRequires:  make
BuildRequires:  zig
BuildRequires:  zig-rpm-macros
BuildRequires:  gnupg2
BuildRequires:  ncurses-devel
BuildRequires:  libzstd-devel

%description
ncdu (NCurses Disk Usage) is a curses-based version of the well-known 'du',
and provides a fast way to see what directories are using your disk space.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q -n ncdu-%{version}
%patch -P0 -p1

%build
%zig_prep
%zig_build -Dpie

%install
%zig_install -Dpie
%{__make} install-doc PREFIX=%{buildroot}%{_prefix}

%files
%{_mandir}/man1/ncdu.1*
%doc ChangeLog
%license LICENSES/MIT.txt
%{_bindir}/ncdu

%changelog
%autochangelog
