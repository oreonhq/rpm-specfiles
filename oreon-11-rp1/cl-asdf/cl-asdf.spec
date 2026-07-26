%global source0_hash 4d32e70f1c26f381ab16fa41062b5b6c38a249030eb5f9b4bc1574482ca53635

Name:    cl-asdf
Version: 20101028
Release: 31%{?dist}
Source:  %{name}-%{version}.tar.bz2
Summary: Another System Definition Facility
URL:     http://www.cliki.net/asdf
License: MIT
BuildArch: noarch
BuildRequires: make
BuildRequires: texinfo-tex

Patch0:  cl-asdf-20101028-texinfo5.patch

%description
Another System Definition Facility (asdf) is a package format for
Common Lisp libraries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n asdf

%install
mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/source/cl-asdf
install -m 644 asdf.lisp %{buildroot}%{_datadir}/common-lisp/source/cl-asdf
install -m 644 wild-modules.lisp %{buildroot}%{_datadir}/common-lisp/source/cl-asdf

%build
cd doc
make

%files
%doc README doc/asdf_html
%{_datadir}/common-lisp/

%changelog
%autochangelog
