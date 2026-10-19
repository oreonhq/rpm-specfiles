%global source0_hash 9b7c87099bb56241ee37ba780d68221f713d51be3f525e3feb3c345bd7a3571f
Name:           LinLog
Version:        0.5
Release:        1%{?dist}
Summary:        A ham radio logbook for Linux
License:        GPL-2.0-only
URL:            http://linlogbook.sourceforge.net/
Source0:        http://downloads.sourceforge.net/linlogbook/linlogbook-%{version}.tar.gz
Source1:        linlogbook.desktop
Source2:        linlogbook.png
Patch0:         LinLog-gcc11.patch
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  make
BuildRequires:  qt4-devel
BuildRequires:  sqlite-devel
# /oreon:deps
%description
LinLogBook is a highly configurable amateur radio logbook for Linux.

It uses an sql-database to store its data. For the ease of use sqlite 3 is
used but it should be possible to use other databases like mysql, for instance.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n linlogbook
%patch -P0 -p1

%build

%{qmake_qt4} -o Makefile linlogbook.pro
make %{?_smp_mflags}
%install
install -p -d %{buildroot}%{_bindir}
install -p -m 755 bin/linlogbook %{buildroot}%{_bindir}/linlogbook
mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/linlogbook.png
desktop-file-install \
        --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
mkdir -p %{buildroot}%{_datadir}/%{name}
install -p -m 644 sql/basetables.sql %{buildroot}%{_datadir}/%{name}
install -p -m 644 sql/example.sql %{buildroot}%{_datadir}/%{name}
install -p -m 644 sql/statistics.sql %{buildroot}%{_datadir}/%{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
