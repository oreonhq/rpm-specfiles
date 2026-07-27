%global source0_hash 48a19679ac7c0530a89657de18ffe49c5759a5ff70fc844928b0e5d00395acae

Name:           librep
Version:        0.92.7
Release:        29%{?dist}
Summary:        A lightweight Lisp environment
License:        GPL-2.0-or-later
URL:            https://github.com/SawfishWM/librep
Source0:        https://deb.debian.org/debian/pool/main/libr/librep/librep_%{version}.orig.tar.xz
Patch0:         librep-configure-c99.patch
Patch1:         gh_new_procedure.patch
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  gdbm-devel
BuildRequires:  readline-devel
BuildRequires:  libffi-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  texinfo
BuildRequires:  chrpath
BuildRequires:  emacs
BuildRequires:  make
Requires:       emacs-filesystem >= %{_emacs_version}

%description
This is a lightweight Lisp environment for UNIX. It contains a Lisp
interpreter, byte-code compiler and virtual machine. Applications may
use the Lisp interpreter as an extension language, or it may be used
for standalone scripts.

Originally inspired by Emacs Lisp, the language dialect combines many
of the Emacs Lisp features while trying to remove some of the main
deficiencies, with features from Common Lisp and Scheme.

%package devel
Summary:        Development files for librep
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
Link libraries and C header files for librep development.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}_%{version}

%build
./autogen.sh --nocfg
%configure --with-readline --enable-shared --disable-static
%make_build
%{_emacs_bytecompile} rep-debugger.el

%install
%make_install
rm -f %{buildroot}%{_infodir}/dir
chrpath --delete %{buildroot}%{_bindir}/rep
install -m 644 rep-debugger.elc %{buildroot}%{_emacs_sitelispdir}
find %{buildroot}%{_libdir} -name \*.la -exec rm '{}' \;

%files
%license COPYING
%doc NEWS README TODO
%{_bindir}/rep
%{_bindir}/rep-remote
%{_libdir}/librep.so.*
%{_libdir}/rep/
%{_datadir}/rep/
%{_datadir}/man/man1/rep-remote.1.gz
%{_datadir}/man/man1/rep.1.gz
%{_infodir}/librep.info.*
%{_emacs_sitelispdir}/rep-debugger.el
%{_emacs_sitelispdir}/rep-debugger.elc
%exclude %{_libdir}/rep/install-aliases
%exclude %{_libdir}/rep/libtool
%exclude %{_libdir}/rep/rules.mk

%files devel
%{_bindir}/rep-xgettext
%{_bindir}/repdoc
%{_includedir}/rep/
%{_libdir}/librep.so
%{_libdir}/pkgconfig/librep.pc
%{_libdir}/rep/install-aliases
%{_libdir}/rep/libtool
%{_libdir}/rep/rules.mk
%{_datadir}/man/man1/rep-xgettext.1.gz
%{_datadir}/man/man1/repdoc.1.gz

%changelog
%autochangelog
