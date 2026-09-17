%global source0_hash c180ac7cc139202645563e91cb209ab62efac5d41a6ed2db4a4730cb71a58275

Name:           dh-make
# Squeeze
Version:        2.202503

Release:        4%{?dist}
Summary:        Tool that converts source archives into Debian package source

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://tracker.debian.org/pkg/dh-make
Source0:        https://ftp.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.xz
BuildArch:      noarch
BuildRequires:      perl-generators

Requires:       debhelper
Requires:       dpkg-dev
Requires:       %{_bindir}/make

%description
This package allows you to take a standard (or upstream) source
package and convert it into a format that will allow you to build
Debian packages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build

%install
mkdir -p %{buildroot}/%{_bindir} %{buildroot}/%{_datadir}/debhelper/dh_make/
install -m 755 dh_make.py %{buildroot}/%{_bindir}/dh_make
install -m 755 dh_makefont %{buildroot}/%{_bindir}
cp -a lib/* %{buildroot}/%{_datadir}/debhelper/dh_make/

# Fix permissions of rules files
find %{buildroot}/%{_datadir}/debhelper/dh_make \
	-type f -name 'rules*' \
	-exec chmod 755 '{}' ';'

find %{buildroot}/%{_datadir}/debhelper/dh_make/debian \
	-type f -name '*.ex' \
	-exec chmod 755 '{}' ';'

mkdir -p %{buildroot}/%{_mandir}/man1
install -m 644 -p dh_make.1 %{buildroot}/%{_mandir}/man1

%files
%doc debian/README.Debian
%{_bindir}/dh_make
%{_bindir}/dh_makefont
%{_mandir}/man1/*.1*
%dir %{_datadir}/debhelper
%{_datadir}/debhelper/dh_make

%changelog
%autochangelog
