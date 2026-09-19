%global source0_hash 1844a35c2d67d54164c81031d1ab72bff2ba5c67eae914baaf0250ee613e2df9

Name:    sugar-write
Version: 101
Release: 16%{?dist}
Summary: Word processor for Sugar
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     http://wiki.sugarlabs.org/go/Activities/Write
Source0: http://download.sugarlabs.org/sources/sucrose/fructose/Write/Write-%{version}.tar.bz2

BuildRequires: gettext
BuildRequires: gobject-introspection-devel
BuildRequires: libabiword-devel
BuildRequires: python3-devel
BuildRequires: python3-abiword
BuildRequires: sugar-toolkit-gtk3-devel

Requires: gobject-introspection
Requires: python3-abiword
Requires: sugar

BuildArch: noarch

%description
The Write activity provides a word processor for the Sugar interface.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -n Write-%{version}

sed -i 's/python/python3/' *.py

%build
python3 ./setup.py build

%install
mkdir -p $RPM_BUILD_ROOT%{sugaractivitydir}
python3 ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}/%{sugaractivitydir}/Write.activity/

%find_lang org.laptop.AbiWordActivity

%files -f  org.laptop.AbiWordActivity.lang
%doc NEWS
%{sugaractivitydir}/Write.activity/

%changelog
%autochangelog
