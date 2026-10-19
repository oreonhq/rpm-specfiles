%global source2_hash 0fe55175b96a8ea1c4b670cc3fe11d56b341e4eff81b161ea49958ae550be6ca
%global source1_hash 286315e100071058b7cb779e222cc7f27b5eb6aa2ea76d45ece1502ac8e08402
%global source0_hash 79d0bb65b82df81c078bc55c4cda3fe4d766d87e3bfe10fde0b2f728204e1015
%undefine _hardened_build
%undefine _package_note_file
%global __brp_strip_lto %{_bindir}/true
%global _lto_cflags %{nil}
Name:           gcl
Version:        2.7.1
Release:        1%{?dist}
Summary:        GNU Common Lisp
License:        LGPL-2.0-or-later AND GPL-1.0-or-later AND MIT-Modern-Variant AND LOOP
URL:            https://www.gnu.org/software/gcl/
VCS:            git:https://git.savannah.gnu.org/git/gcl.git
Source0:        https://ftp.gnu.org/gnu/gcl/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/gcl/%{name}-%{version}.tar.gz.sig
Source2:        https://ftp.gnu.org/gnu/gnu-keyring.gpg
Source3:        gcl.el
%global patchdir %{version}-18
Patch:          %{name}-2.7.1-errata.patch
Patch:          %{name}-2.6.11-latex.patch
Patch:          %{name}-2.7.1-texinfo.patch
Patch:          %{name}-2.7.1-elisp.patch
Patch:          %{name}-2.7.1-format.patch
Patch:          %{name}-2.7.1-bsearch.patch
ExcludeArch:    %{ix86}
Requires:       gcc
Requires:       libtirpc-devel%{?_isa}
Requires:       util-linux%{?_isa}
Requires:       which%{?_isa}
# oreon:deps
BuildRequires:  binutils-devel
BuildRequires:  bzip2
BuildRequires:  emacs-nw
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  gpgverify
BuildRequires:  make
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(tcl)
BuildRequires:  pkgconfig(tk)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  tex(latex)
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
BuildRequires:  texlive-ec
# /oreon:deps
%description
GCL is a Common Lisp currently compliant with the ANSI standard.  Lisp
compilation produces native code through the intermediary of the system's C
compiler, from which GCL derives efficient performance and easy portability.
The GUI currently uses TCL/Tk.

%package emacs
License:        GPL-1.0-or-later
Summary:        Emacs mode for interacting with GCL
Requires:       %{name} = %{version}-%{release}
Requires:       emacs(bin) %{?_emacs_version:>= %{_emacs_version}}
BuildArch:      noarch
%description emacs
Emacs mode for interacting with GCL

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}
%autosetup -p1

%conf
# Ensure the frame pointer doesn't get added back
sed -i 's/"-fomit-frame-pointer"/""/' configure

# Silence warnings about the obsolescence of egrep
sed -i 's/egrep/grep -E/' ltmain.sh

# Fix path to the saved images
sed -i 's,/lib/,/%{_lib}/,' bin/gcl.in

# Get a version of texinfo.tex that works with the installed version of texinfo
cp -p %{_texmf_main}/tex/texinfo/texinfo.tex info

# The archive is so full of spurious executable bits that we just remove them
# all here, then add back the ones that should exist
find . -type f -perm /0111 -exec chmod a-x {} +
chmod a+x ansi-tests/make-tar compile config.guess config.sub configure \
  depcomp gcl-tk/gcltksrv.in install-sh missing xbin/*

# Temporary workaround for problems detecting architecture.  Remove this on the
# next release.
%ifarch %{power64}
sed -i 's,output_mach=`.*`,output_mach=ppc64,' configure
%endif
%ifarch s390x
sed -i 's,output_mach=`.*`,output_mach=s390_64,' configure
%endif

%build

%configure \
  --disable-dependency-tracking \
  --enable-readline \
  --enable-tcltk \
  --enable-tclconfig=%{_libdir} \
  --enable-tkconfig=%{_libdir} \
  --enable-xdr \
  --enable-xgcl
make
rm info/gcl.info
make -C info gcl.info
cd xgcl-2
pdflatex dwdoc.tex
pdflatex dwdoc.tex
cd -
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc
rm -rf $RPM_BUILD_ROOT%{_datadir}/emacs
rm -rf $RPM_BUILD_ROOT%{_prefix}/lib/gcl-*/info
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cp -pf man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_emacs_sitelispdir}/gcl
cp -pfr elisp/* $RPM_BUILD_ROOT%{_emacs_sitelispdir}/gcl
rm -f $RPM_BUILD_ROOT%{_emacs_sitelispdir}/gcl/makefile
rm -f $RPM_BUILD_ROOT%{_emacs_sitelispdir}/gcl/readme
mkdir -p $RPM_BUILD_ROOT%{_emacs_sitestartdir}
sed -e "s|%LISP_DIR%|%{_emacs_sitelispdir}|" %{SOURCE3} > $RPM_BUILD_ROOT%{_emacs_sitestartdir}/gcl.el
pushd $RPM_BUILD_ROOT%{_emacs_sitelispdir}/gcl
%{_emacs_bytecompile} *.el
popd
ln -s ../h/cmpinclude.h cmpnew/cmpinclude.h
ln -s ../h/cmpinclude.h lsp/cmpinclude.h
ln -s ../h/cmpinclude.h xgcl-2/cmpinclude.h
chmod 0755 %{buildroot}%{_libdir}/gcl-%{version}/unixport/libboot.so
export QA_SKIP_BUILD_ROOT=1
%clean
rm -f /tmp/gazonk_* /tmp/gcl_*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gcl-emacs -f %{oreon_filedir}/gcl-emacs.list

%changelog

%autochangelog
