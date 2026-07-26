%global source0_hash e8e3acb253c64394f35c8e17942f764cae34df731f3fe3d749b6a2ae1fb8203b

Name:           saclib
Version:        2.2.8
Release:        11%{?dist}
Summary:        Computer algebra library

License:        ISC
URL:            https://www.usna.edu/Users/cs/wcbrown/qepcad/B/QEPCAD.html
Source0:        https://www.usna.edu/Users/cs/wcbrown/qepcad/INSTALL/%{name}%{version}.tgz
# The sources include system-dependent definitions.  The Linux versions support
# only x86 and x86_64.  These versions should work on any Linux system.
Source1:        GC.c
Source2:        sysdep.h
# Add function prototypes and attributes for better optimization. Upstream:
# 20 Nov 2013.
Patch:          %{name}-attr.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tex(latex)

%global major %(cut -d. -f1 <<< %{version})

%description
SACLIB is a library of C programs for computer algebra derived from the SAC2
system.  Hoon Hong was the primary author of that earlier system.

%package devel
# The content is ISC.  The remaining licenses cover the various fonts embedded
# in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
License:        ISC AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later
Summary:        Development files for saclib
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and library links for developing applications that use saclib.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}%{version} -p0
cp -p %{SOURCE1} src
cp -p %{SOURCE2} include

%conf
# Generate the makefile
saclib=$PWD bin/mkmake

# Build a shared library instead of a static library and link with -lm
sed -e 's/saclib\${EXTENSION}\.a/libsaclib.so/' \
    -e 's/\${RANLIB}.*/& ${OBJS1} ${OBJS2a} ${OBJS2b} ${OBJS3} ${OBJS4} -lm/' \
    -i lib/objo/makefile

%build
export saclib=$PWD
export CFLAGS='%{build_cflags} -frounding-math'
%make_build -C lib/objo SACFLAG="$CFLAGS -fPIC" AR=true \
  RANLIB="gcc -shared $CFLAGS %{build_ldflags} -Wl,-h,libsaclib.so.%{major} -o"

# Build the documentation
cd doc/user_guide
rm *.{aux,dvi,ilg,ind,log,toc,lof,pdf}
pdflatex saclocal
pdflatex saclocal
pdflatex sackwic
pdflatex saclib
makeindex saclib
pdflatex saclib
pdflatex saclib

%install
# Install the library
mkdir -p %{buildroot}%{_libdir}
install -p -m 0755 lib/libsaclib.so %{buildroot}%{_libdir}/libsaclib.so.%{version}
ln -s libsaclib.so.%{version} %{buildroot}%{_libdir}/libsaclib.so.%{major}
ln -s libsaclib.so.%{major} %{buildroot}%{_libdir}/libsaclib.so

# Install the headers
mkdir -p %{buildroot}%{_includedir}/%{name}
cp -p include/*.h %{buildroot}%{_includedir}/%{name}

%files
%doc README
%license LICENSE
%{_libdir}/libsaclib.so.2{,.*}

%files devel
%doc doc/user_guide/*.pdf
%{_includedir}/%{name}/
%{_libdir}/libsaclib.so

%changelog
%autochangelog
