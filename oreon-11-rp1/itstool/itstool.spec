%global source0_hash fba78a37dc3535e4686c7f57407b97d03c676e3a57beac5fb2315162b0cc3176

Name:           itstool
Version:        2.0.7
Release:        12%{?dist}
Summary:        ITS-based XML translation tool

License:        GPL-3.0-or-later
URL:            http://itstool.org/
Source0:        https://github.com/itstool/itstool/archive/refs/tags/%{version}.tar.gz#/itstool-%{version}.tar.gz
# See:  https://github.com/itstool/itstool/issues/25
Patch0:        https://sources.debian.org/data/main/i/itstool/2.0.5-2/debian/patches/fix_crash_912099.patch#/itstool-2.0.5-fix-crash-wrong-encoding.patch
# Filed upstream at https://github.com/itstool/itstool/pull/51
Patch1:        https://src.fedoraproject.org/rpms/itstool/raw/rawhide/f/0001-Fix-insufficiently-quoted-regular-expressions.patch

BuildArch:      noarch

BuildRequires:  python3-libxml2
BuildRequires:  python3-devel
BuildRequires: make
Requires:       python3-libxml2

%description
ITS Tool allows you to translate XML documents with PO files, using rules from
the W3C Internationalization Tag Set (ITS) to determine what to translate and
how to separate it into PO file messages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P0 -p1 -b .encoding
%patch -P1 -p1 -b .py312-regex

%build
export PYTHON=%{__python3}
%configure
%make_build

%install
%make_install

%files
%license COPYING COPYING.GPL3
%doc NEWS
%{_bindir}/itstool
%{_datadir}/itstool
%{_mandir}/man1/itstool.1*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.7-12
- Import
