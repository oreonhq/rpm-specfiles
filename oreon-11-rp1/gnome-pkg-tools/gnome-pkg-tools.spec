%global source0_hash 6fe2ef005b9c4bd9d592cdef2ae69de4587765cbe9fe9649f740297c7b6ccbd6

Name:           gnome-pkg-tools
Version:        0.22.13
Release:        2%{?dist}
Summary:        Tools for the Debian GNOME Packaging Team

BuildArch:      noarch
License:        GPL-2.0-or-later
URL:            http://packages.debian.org/unstable/%{name}
Source0:        http://ftp.de.debian.org/debian/pool/main/g/%{name}/%{name}_%{version}.tar.xz

BuildRequires:  perl-generators
Requires:       debhelper

%description
This package contains some tools useful for the Debian GNOME Packaging Team
including:
 * Documentation.
 * The list of team members.
 * A number of rules files for CDBS that are helpful for GNOME
   packages - but may also be useful for others.
This package is useful when building Debian packages on Fedora, for instance
via pbuilder.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -C

%build
# Nothing to build

%install
install -Dpm 0755 dh/dh_gnome %{buildroot}%{_bindir}/dh_gnome
install -d %{buildroot}%{_datadir}/%{name}
cp -a 1 %{buildroot}%{_datadir}/%{name}/1
install -Dpm 0644 dh/dh_gnome.1 %{buildroot}%{_mandir}/man1/dh_gnome.1
install -Dpm 0755 dh/gnome.pm %{buildroot}%{perl_vendorlib}/Debian/Debhelper/Sequence/gnome.pm

%files
%doc debian/README.Debian
%license debian/copyright
%{_bindir}/dh_gnome
%{_datadir}/%{name}/
%{_mandir}/man1/dh_gnome.1*
%{perl_vendorlib}/Debian/Debhelper/Sequence/gnome.pm

%changelog
%autochangelog
