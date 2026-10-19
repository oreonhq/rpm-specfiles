%global source1_hash acc417c04795fff819a516520dc0d976eb15f3789d041abcf77a1fd52fb24891
%global source0_hash 6301592b0020c14b456757ef5d434d49f6027b8e5f3a499d13362f205c486e0e
Name:		recutils
Version:	1.9
Release:        13%{?dist}
Summary:        A set of tools to access GNU recfile databases
License:	GPL-3.0-or-later
URL:		https://www.gnu.org/software/recutils/
Source0:        https://ftp.gnu.org/gnu/recutils/%{name}-%{version}.tar.gz
Source1:	https://ftp.gnu.org/gnu/recutils/%{name}-%{version}.tar.gz.sig
Source2:	gpgkey-BDFA5717FC1DD35C2C3832A23EF90523B304AF08.gpg
Source3:	rec-mode-v1.8.3.tar.gz
Source4:	rec-mode-init.el
Patch1:		recutils-1.9-mdbtools-0.9.patch
Patch2:		recutils-c99.patch
Requires:	emacs(bin) >= %{_emacs_version}
Provides: bundled(gnulib)
# oreon:deps
BuildRequires:  bison
BuildRequires:  chrpath
BuildRequires:  emacs-nox
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  help2man
BuildRequires:  libgcrypt-devel
BuildRequires:  make
BuildRequires:  mdbtools-devel
BuildRequires:  texinfo
# /oreon:deps
%description
Recutils is a set of tools and libraries to access human-editable,
text-based databases called recfiles. The data is stored as a sequence
of records, each record containing an arbitrary number of named
fields.

%package devel
Summary:	Libraries and header files for recutils
Requires:	%{name} = %{version}-%{release}
%description devel
Libraries and header files for recutils

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
# mdbtools >= 0.9.0 no longer has mdb_init
sed -i 's/mdb_init/mdb_open/' configure
tar xf %{SOURCE3}

%build

%configure --disable-static --disable-rpath
%make_build
%{_emacs_bytecompile} rec-mode/*.el
%check

make check
%install
%make_install INSTALL="install -p"
install -dm 755 %{buildroot}%{_emacs_sitelispdir}
install -pm 644 rec-mode/*.el* %{buildroot}%{_emacs_sitelispdir}
install -dm 755 %{buildroot}/%{_emacs_sitestartdir}
install -pm 644 %{SOURCE4} %{buildroot}/%{_emacs_sitestartdir}
install -pm 644 rec-mode/rec-mode.info %{buildroot}%{_infodir}
rm -f %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_libdir}/*.la
chrpath --delete %{buildroot}%{_bindir}/*
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n recutils-devel -f %{oreon_filedir}/recutils-devel.list

%changelog

%autochangelog
