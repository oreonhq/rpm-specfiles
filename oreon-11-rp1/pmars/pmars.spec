%global source0_hash 2ae8638ec6b65350cf9f813a60e338b534dffa78c3e85f1823a2bee8b7c20a34

Name:           pmars
Version:        0.9.2
Release:        37%{?dist}
Summary:        Portable corewar system with ICWS'94 extensions

License:        GPL-2.0-or-later
URL:            http://www.koth.org/pmars/
Source0:        http://downloads.sourceforge.net/corewar/%{name}-%{version}.tar.gz
# Patch to disable stripping of binary in spec file
Patch0:         pmars-0.9.2-nostrip.patch
#Show compiler commands
Patch1:         pmars-0.9.2-CCat.patch
Patch2:         pmars-sfprintf-format.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  libX11-devel
Requires:       xorg-x11-fonts-75dpi

%description
pMARS is a Memory Array Redcode Simulator (MARS) for corewar.

    * portable, run it on your Mac at home or VAX at work
    * free and comes with source
    * core displays for DOS, Mac and UNIX
    * implements a new redcode dialect, ICWS'94, while remaining compatible
      with ICWS'88
    * powerful redcode extensions: multi-line EQUates, FOR/ROF text repetition
    * one of the fastest simulators written in a high level language
    * full-featured, programmable debugger
    * runs the automated tournament "KotH" at http://www.koth.org and
      http://www.ecst.csuchico.edu/~pizza/koth/ and the annual ICWS tournaments

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0 -b .nostrip
%patch -P1 -p0 -b .CCat
%patch -P2 -p0 -b .printf

# Make temporary doc dir
mkdir doc_install
cp -a doc doc_install
rm doc_install/doc/pmars.6

%build
%global build_type_safety_c 0
make -C src CFLAGS="%{optflags} -DEXT94 -DXWINGRAPHX -DPERMUTATE -std=gnu17"

%install
rm -rf %{buildroot}
install -D -p -m 755 src/pmars %{buildroot}%{_bindir}/pmars
install -D -p -m 644 doc/pmars.6 %{buildroot}%{_mandir}/man6/pmars.6

%files
%doc AUTHORS ChangeLog CONTRIB COPYING README config/ doc_install/doc/ warriors/
%{_bindir}/pmars
%{_mandir}/man6/pmars.6.*

%changelog
%autochangelog
