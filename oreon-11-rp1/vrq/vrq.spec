%global source0_hash 7f4bed1b7f6e7ab6604eba8da555b3915596f1024db8aa24e1fd4ff94dc6290e

Name:           vrq
Version:        1.0.134
Release:        15%{?dist}
Summary:        Verilog tool framework with plugins for manipulating source code

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://vrq.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         vrq-gcc11.patch

# ---- Exclusive Arch: ----
# plugin/sim uses x86 inline assembly

ExclusiveArch:  %{ix86} x86_64

BuildRequires: make
BuildRequires:  bison
BuildRequires:  bzip2-devel
BuildRequires:  doxygen
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  iverilog
BuildRequires:  libtool-ltdl-devel
BuildRequires:  man2html-core
BuildRequires:  perl-Time-HiRes
BuildRequires:  readline-devel
BuildRequires:  zlib-devel

%description
VRQ is modular verilog parser that supports plugin tools to process verilog. 
Multiple tools may be invoked in a pipeline fashion within a single execution 
of vrq. It is a generic front-end parser with support for plugin backend 
customizable tools.

%package devel
Summary:        Header files and libraries for Vrq development
Requires:       %{name} = %{version}-%{release}

%description devel
The vrq-devel package contains the header files and libraries needed
to develop backend plugin customization tools for the vrq tool framework.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
%{__rm} -rf `find . -name CVS`
%{__rm} -f `find . -name *.o`
%{__rm} -f `find . -name *.so`

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%configure
%make_build

%install
%make_install
%{__rm} -f `find %{buildroot} -name *.la`
%{__rm} -rf `find %{buildroot} -name latex`

# add some doc files into the buildroot manually (#992864)
for f in AUTHORS ChangeLog COPYING README doc/faq.html ; do
    install -p -m0644 -D $f %{buildroot}%{_docdir}/%{name}/${f}
done

install -d -m0755 %{buildroot}%{_docdir}/%{name}/doc
cp -pr doc/html %{buildroot}%{_docdir}/%{name}/doc

install -d -m0755 %{buildroot}%{_docdir}/%{name}/plugin
cp -pr plugin/examples %{buildroot}%{_docdir}/%{name}/plugin

rm -rf %{buildroot}%{_docdir}/%{name}-%{version}

%files
%dir %{_docdir}/%{name}
%dir %{_docdir}/%{name}/doc
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/ChangeLog
%{_docdir}/%{name}/COPYING
%{_docdir}/%{name}/README
%{_docdir}/%{name}/doc/faq.html
%{_bindir}/%{name}
%{_libdir}/%{name}-%{version}
%{_mandir}/man1/vrq.1.gz

%files devel
%{_docdir}/%{name}/doc/html
%{_docdir}/%{name}/plugin/examples
%{_includedir}/%{name}-%{version}

%changelog
%autochangelog
