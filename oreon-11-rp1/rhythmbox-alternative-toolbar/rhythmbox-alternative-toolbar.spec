%global source2_hash 5f521b0e0a21ddb5edfbdbefae792a6dda45f7a5e7465ff78e19374e8997accd
%global source0_hash d2beaa901a9419948a247966332f56fe6f053b28371932a7b05089cefe7e0b9b
%global debug_package %{nil}
%global mod_name alternative-toolbar
Name:		rhythmbox-alternative-toolbar
Version:	0.21.0
Release:        1%{?dist}
Summary:        Client-side decorated compact toolbar for Rhythmbox
License:	GPL-3.0-or-later
URL:		https://github.com/fossfreedom/alternative-toolbar
Source0:        https://github.com/fossfreedom/%{mod_name}/releases/download/v%{version}/%{mod_name}-%{version}.tar.xz
Source1:	%{url}/releases/download/v%{version}/%{mod_name}-%{version}.tar.xz.asc
Source2:	https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x1e1fb0017c998a8ae2c498a6c2eaa8a26adc59ee#/1E1FB0017C998A8AE2C498A6C2EAA8A26ADC59EE.gpg
Patch0:		https://github.com/fossfreedom/alternative-toolbar/commit/8a379a970ceb2ce080ddb80d28dc2de009273064.patch
Requires:	rhythmbox
ExcludeArch:	s390 s390x
# oreon:deps
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gnupg2
BuildRequires:  gobject-introspection
BuildRequires:  gtk3
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  python3-gobject
BuildRequires:  rhythmbox-devel
# /oreon:deps
%description
Alternative Toolbar replaces the Rhythmbox large toolbar with a Client-Side
Decorated or Compact toolbar which can be hidden.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{mod_name}-%{version} -p1

%build

%configure
%make_build
%install
%make_install
rm -f %{buildroot}%{_libdir}/rhythmbox/plugins/%{mod_name}/LICENSE
%find_lang %{mod_name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
