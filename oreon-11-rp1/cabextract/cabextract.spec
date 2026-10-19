%global source0_hash b5546db1155e4c718ff3d4b278573604f30dd64c3c5bfd4657cd089b823a3ac6
Name:           cabextract
Version:        1.11
Release:        10%{?dist}
Summary:        Utility for extracting cabinet (.cab) archives
%if 0%{?mspack}
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
%else
License:        GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only
%endif
URL:            https://www.cabextract.org.uk/
Source0:        https://www.cabextract.org.uk/%{name}-%{version}.tar.gz
%if 0%{?mspack}
%else
Provides: bundled(libmspack) = 0.11-0.1.alpha.modified_by_cabextract
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
cabextract is a program which can extract files from cabinet (.cab)
archives.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
  %{?mspack:--with-external-libmspack}
%make_build
%check

%make_build check
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
