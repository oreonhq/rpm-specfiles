%global source0_hash d14402f93d3c808fba91ff0d54fe2e536912f40cf9cab365368e722890210b55

Name:           Saaghar
Version:        3.0.0
Release:        25%{?dist}
Summary:        A Cross-Platform Persian Poetry Software

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://pozh.org/saaghar/
Source0:        https://github.com/srazi/Saaghar/releases/download/v%{version}/Saaghar-%{version}.tar.gz
# Fedora specific: do not install doc files
Patch0:         %{name}-installfix.patch

BuildRequires: make
BuildRequires:  gcc-c++ qt-devel desktop-file-utils phonon-devel
Recommends:     %{name}-data

%description
Saaghar is a cross-platform Persian poetry software. It uses 
http://ganjoor.net database. It has lots of features:
* Tabbed UI
* Tabbed and dock-able search widgets
* Print and Print Preview
* Export, It supports exporting to "PDF", "HTML", "TeX", "CSV" and "TXT"
* Copy and Multi-selection
* Customisable interface

%package        data
Version:        67.92.11
Release:        24.%{release}
Summary:        Database for %{name}
BuildArch:      noarch
Source1:        http://downloads.sourceforge.net/saaghar/%{name}-data-%{version}.xz

%description    data
This package contains the database for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}
%patch -P0 -p1 -b .installfix
xz -dc %{SOURCE1} > data/ganjoor.s3db
chmod a-x data/Saaghar.desktop
sed -i.dosfix "s/\r//g" data/Saaghar.desktop
rm -rf data/fonts/

%build
%{qmake_qt4} -config release
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}
install -Dp -m 0644 data/ganjoor.s3db %{buildroot}%{_datadir}/saaghar/

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%doc AUTHORS GPLv3 CHANGELOG README.md TODO LICENSE
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_datadir}/saaghar/themes
%{_datadir}/saaghar/*.pdf
%{_datadir}/saaghar/*.qm
%{_datadir}/saaghar/*.gdb
%dir %{_datadir}/saaghar

%files data
%{_datadir}/saaghar/ganjoor.s3db

%changelog
%autochangelog
