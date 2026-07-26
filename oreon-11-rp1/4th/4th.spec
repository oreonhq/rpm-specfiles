%global source0_hash f822f7dd8cfb0b1744a62d653c6efe933578ae1789ec60a088509a38bca4b4fc

Name:           4th
Version:        3.62.5
Release:        23%{?dist}
Summary:        A Forth compiler

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://thebeez.home.xs4all.nl/4tH/
Source0:        https://downloads.sourceforge.net/project/forth-4th/%{name}-%{version}/%{name}-%{version}-unix.tar.gz

BuildRequires:  gcc make

%description
4tH is basic framework for creating application specific scripting
languages. It is a library of functions centered around a virtual
machine, which guarantees high performance, ease of use and low overhead.

%package devel
Summary:        Development files for 4th
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package includes headers for development with 4th, a Forth compiler
library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}-unix

%build
LD_LIBRARY_PATH="$PWD/sources/" \
make %{?_smp_mflags} -C sources \
        STATIC= SHARED=1 \
        CFLAGS="-DUNIX -fsigned-char %{optflags} -fPIC"

%install
mkdir -p \
        %{buildroot}%{_libdir} \
        %{buildroot}%{_includedir}/%{name} \
        %{buildroot}%{_bindir} \
        %{buildroot}%{_mandir} \
        %{buildroot}%{_docdir}/%{name}

LD_LIBRARY_PATH="$PWD/sources/" \
%make_install -C sources \
        STATIC= SHARED=1 \
        LIBRARIES=%{buildroot}%{_libdir} \
        INCLUDES=%{buildroot}%{_includedir} \
        BINARIES=%{buildroot}%{_bindir} \
        MANDIR=%{buildroot}%{_mandir} \
        DOCDIR=%{buildroot}%{_docdir}
cp -ap sources/include/*.h %{buildroot}%{_includedir}/%{name}/

%files
%{_libdir}/lib4th.so.3*
%{_bindir}/4tsh
%{_bindir}/pp4th
%{_bindir}/4th
%{_mandir}/man1/4th.1*
%doc %{_docdir}/%{name}
%doc README
%license COPYING

%files devel
%{_libdir}/lib4th.so
%{_includedir}/%{name}

%changelog
%autochangelog
