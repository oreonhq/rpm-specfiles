%global source0_hash 3d16f1ce3373ed96419ba57399c2e4d94f88613c2cb4968cb0331ecac3da68bd
%global makedocs 0
Name:          lout
Summary:        A document formatting system
Version:       3.40
Release:        1%{?dist}
License:       GPL-2.0-or-later
URL:           http://savannah.nongnu.org/projects/lout/
Source0:        http://download.savannah.gnu.org/releases/lout/lout-%{version}.tar.gz
%if !%{makedocs}
Source1:       design.pdf
Source2:       expert-guide.pdf
Source3:       user-guide.pdf
Source4:       slides.pdf
%endif
Patch0:        makefile.patch
Patch1:        fix-FSF-address.patch
Patch2:         lout-3.40-cve.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  ghostscript
BuildRequires:  make
# /oreon:deps
%description
Lout is a document formatting system designed and implemented by Jeffrey
Kingston at the Basser Department of Computer Science, University of
Sydney, Australia. The system reads a high-level description of a document
similar in style to LaTeX and produces a PostScript file which can be
printed on most laser printers and graphic display devices. Plain text
output is also available, PDF output is limited but working (e.g. no
graphics). Lout is inherently multilingual. Adding new languages is easy.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build

make COPTS="$RPM_OPT_FLAGS" \
     BINDIR=%{_bindir} \
     LOUTLIBDIR=%{_datadir}/%{name} \
     LOUTDOCDIR=%{_datadir}/%{name}/doc \
     MANDIR=%{_mandir}/man1 \
     prg2lout lout
function render_docs {
    subdir=$1
    pdf_file=$2
    passes=$3
    curdir=$(pwd)
    pushd doc/$subdir
    PATH=$curdir lout \
       -I $curdir/include \
       -D $curdir/data \
       -F $curdir/font \
       -H $curdir/hyph \
       -C $curdir/maps \
       -r${passes} all > outfile.ps
    ps2pdf outfile.ps ../${pdf_file}
    rm *.li *.ld outfile.ps
    popd
}
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} doc/
%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}/doc
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
make BINDIR=$RPM_BUILD_ROOT%{_bindir} \
     LOUTLIBDIR=$RPM_BUILD_ROOT%{_datadir}/%{name} \
     LOUTDOCDIR=$RPM_BUILD_ROOT%{_datadir}/%{name}/doc \
     MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
     install installman installdoc
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
