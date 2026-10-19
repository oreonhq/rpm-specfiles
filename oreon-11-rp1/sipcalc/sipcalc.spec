%global source0_hash cfd476c667f7a119e49eb5fe8adcfb9d2339bc2e0d4d01a1d64b7c229be56357
Name: sipcalc
Version: 1.1.6
Release:        1%{?dist}
Summary:        An "advanced" console based ip subnet calculator
License: BSD-3-Clause
URL: http://www.routemeister.net/projects/sipcalc
Source0:        http://www.routemeister.net/projects/%{name}/files/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Sipcalc is an "advanced" console based ip subnet calculator.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1
autoreconf --verbose --force --install

# convert ChangeLog to UTF-8
iconv -f ISO-8859-1 -t UTF-8 ChangeLog > ChangeLog.utf8 && \
touch -r ChangeLog ChangeLog.utf8 && \
mv -f ChangeLog{.utf8,}

%build

%configure
%make_build
%install
%make_install DESTDIR=%{buildroot} INSTALL="install -p"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
