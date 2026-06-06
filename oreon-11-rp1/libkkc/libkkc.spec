%global source0_hash 89b07b042dae5726d306aaa1296d1695cb75c4516f4b4879bc3781fe52f62aef

%global dataversion 1:0.2.7

Name:		libkkc
Version:	0.3.5
Release:	34%{?dist}
Summary:	Japanese Kana Kanji conversion library

License:	GPL-3.0-or-later
URL:		https://github.com/ueno/libkkc
Source0:        https://github.com/ueno/libkkc/releases/download/v%{version}/%{name}-%{version}.tar.gz
# remove for next release:
Source1:        https://raw.githubusercontent.com/ueno/libkkc/HEAD/README.md
Patch0:        libkkc-HEAD.patch
Patch1:        libkkc-POT.skip.patch
Patch2:        libkkc-vala-abstract-create.patch
# https://github.com/ueno/libkkc/pull/40
# Fix compilation with gcc14 -Werror=int-conversion
Patch3:        libkkc-pr40-int-conversion-fix.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2306455
# Fix invalid escape on default.json
Patch4:        libkkc-Fix-invalid-escape-on-json-file.patch
Patch5:        libkkc-use-gettext.patch

BuildRequires:  gcc-c++
BuildRequires:	marisa-devel
BuildRequires:	vala
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	json-glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-common
BuildRequires:	python3-devel
BuildRequires:	python3-marisa
BuildRequires:  make
BuildRequires:  chrpath
BuildRequires:  autoconf, autoconf-archive

Requires:	skkdic
Requires:	%{name}-data >= %{dataversion}
Requires:	%{name}-common = %{version}-%{release}

%description
libkkc provides a converter from Kana-string to
Kana-Kanji-mixed-string.  It was named after kkc.el in GNU Emacs, a
simple Kana Kanji converter, while libkkc tries to convert sentences
in a bit more complex way using N-gram language models.


%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        tools
Summary:	Tools for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	tools
The %{name}-tools package contains tools for developing applications
that use %{name}.


%package	common
Summary:	Common data files for %{name}
BuildArch:	noarch

%description	common
The %{name}-common package contains the arch-independent data that
%{name} uses at run time.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

[ -f README.md ] || cp -p %SOURCE1 .
gnome-autogen.sh


%build
%configure --disable-static --disable-silent-rules PYTHON=python3
%make_build


%check
make check


%install
%make_install

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# https://bugzilla.redhat.com/show_bug.cgi?id=1987650
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/kkc

%find_lang %{name}


%files -f %{name}.lang
%doc README data/rules/README.rules COPYING
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/*.typelib

%files common
%{_datadir}/libkkc

%files devel
%doc
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/vala/vapi/*

%files tools
%{_bindir}/kkc*


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.5-34
- Import
