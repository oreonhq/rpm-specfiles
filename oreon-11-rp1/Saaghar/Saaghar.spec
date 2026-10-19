%global source1_hash a4be795e6c7d3a88b99f2f5d79711bf5860db7cd5f033cc37b0e0ae614671c49
%global source0_hash 62ed14604aaf35f906735ba73d4b55df9f9d000d36603e4edbe50c7c2a76e898
Name:           Saaghar
Version:        3.0.0
Release:        25%{?dist}
Summary:        A Cross-Platform Persian Poetry Software
License:        GPL-3.0-or-later
URL:            http://pozh.org/saaghar/
Source0:        https://github.com/srazi/Saaghar/releases/download/v%{version}/Saaghar-%{version}.tar.gz
Patch0:         %{name}-installfix.patch
Recommends:     %{name}-data
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  phonon-devel
BuildRequires:  qt-devel
# /oreon:deps
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
%oreon_autofiles Saaghar-data usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n Saaghar-data -f %{oreon_filedir}/Saaghar-data.list

%changelog

%autochangelog
