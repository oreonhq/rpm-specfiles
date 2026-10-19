%global source0_hash 9029faecc9675de656d956d572b4e97bc6a794779ddd50b7f9bb2f92597ad47e
%define version_major 0.96
%define version_minor 11
Name:           corrida
Version:        %{version_major}.%{version_minor}
Release:        1%{?dist}
Summary:        Application for archivation of meteor observations
License:        GPL-2.0-only
URL:            http://corrida.pkim.org/
Source0:        http://%{name}.pkim.org/releases/%{name}-%{version_major}-%{version_minor}.tar.gz
Source1:        corrida.desktop
Patch0:         corrida-0.96-11-count.patch
Patch1:         corrida-0.96-11-formatsec.patch
Patch2: corrida-c99.patch
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  make
# /oreon:deps
%description
Application was designed by Polish Fireball Center cooperators to ease
archivation of meteor observations.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n corrida-%{version_major}-%{version_minor}
%patch -P0 -p1 -b .count
%patch -P1 -p1 -b .formatsec
%patch -P2 -p1

%build

find . -type f |xargs chmod 0644
make %{?_smp_mflags} PREFIX=%{_prefix}/ CFLAGS="%{optflags}"
convert common/corrida.ico corrida.png
%install
make install PREFIX=%{buildroot}%{_prefix}/
install -d %{buildroot}%{_datadir}/pixmaps
install -d %{buildroot}%{_datadir}/applications
install -pm 0644 corrida.png %{buildroot}%{_datadir}/pixmaps
desktop-file-install %{SOURCE1} \
        --dir=%{buildroot}%{_datadir}/applications
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
