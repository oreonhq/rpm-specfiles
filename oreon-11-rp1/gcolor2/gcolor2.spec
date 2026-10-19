%global source0_hash 0613c4c0e5e9bbf8a579d40d63ed8066d272e73d6ed3491d73aba5ce37293bea
Name:           gcolor2
Version:        0.4
Release:        1%{?dist}
Summary:        A simple color selector for GTK+2
License:        GPL-2.0-only
URL:            http://gcolor2.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Patch0:         %{name}-0.4-missing-includes.patch
Patch1:         %{name}-0.4-ftbfs.patch
Patch2:         %{name}-0.4-gcc10.patch
Patch3:         gcolor2-configure-c99.patch
Patch4:         gcolor2-c99.patch
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 11 || 0%{?oreon} >= 11
ExcludeArch:    %{ix86}
%endif
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  make
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl-interpreter
# /oreon:deps
%description
gcolor2 is a simple color selector that was originally based on gcolor, 
ported to use GTK+2, and now has a completely new UI. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# make sure path to icon is correct
sed -i 's!/usr/share!%{_datadir}!' %{SOURCE1}

%build

%configure
%make_build
%install
%make_install
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
