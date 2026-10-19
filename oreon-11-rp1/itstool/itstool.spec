%global source0_hash fba78a37dc3535e4686c7f57407b97d03c676e3a57beac5fb2315162b0cc3176
Name:           itstool
Version:        2.0.7
Release:        1%{?dist}
Summary:        ITS-based XML translation tool
License:        GPL-3.0-or-later
URL:            http://itstool.org/
Source0:        https://github.com/itstool/itstool/archive/refs/tags/%{version}.tar.gz#/itstool-%{version}.tar.gz
Patch0:        https://sources.debian.org/data/main/i/itstool/2.0.5-2/debian/patches/fix_crash_912099.patch#/itstool-2.0.5-fix-crash-wrong-encoding.patch
Patch1:        0001-Fix-insufficiently-quoted-regular-expressions.patch
BuildArch:      noarch
Requires:       python3-libxml2
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-libxml2
# /oreon:deps
%description
ITS Tool allows you to translate XML documents with PO files, using rules from
the W3C Internationalization Tag Set (ITS) to determine what to translate and
how to separate it into PO file messages.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P0 -p1 -b .encoding
%patch -P1 -p1 -b .py312-regex
autoreconf -fi

%build

export PYTHON=%{__python3}
%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.7-12
- Import
