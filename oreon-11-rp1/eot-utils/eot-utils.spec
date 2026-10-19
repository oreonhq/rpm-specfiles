%global source0_hash 4eed49dac7052e4147deaddbe025c7dfb404fc847d9fe71e1c42eba5620e6431
%bcond autoreconf 1
Name:           eot-utils
Version:        1.1
Release:        1%{?dist}
Summary:        Create or examine EOT font format files
License:        W3C
SourceLicense:  %{shrink:
                %{license} AND
                FSFUL AND
                FSFULLR AND
                GPL-2.0-or-later AND
                X11
                }
URL:            https://www.w3.org/Tools/eot-utils/
Source0:        https://www.w3.org/Tools/%{name}//eot-utilities-%{version}.tar.gz
ExcludeArch:    %{ix86}
%if %{with autoreconf}
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
The eot-utils are the two programs mkeot and eotinfo. The former creates an EOT
(Embedded OpenType) file from an OpenType or TrueType font and the URLs of one
or more Web pages, respecting the TrueType embedding bits. The eotinfo program
displays EOT metadata in a human-readable way.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n eot-utilities-%{version}

%conf
%if %{with autoreconf}
autoreconf --force --install --verbose
%endif
%configure

%build

%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
