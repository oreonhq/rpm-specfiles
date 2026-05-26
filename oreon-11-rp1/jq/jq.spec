# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 2be64e7129cecb11d5906290eba10af694fb9e3e7f9fc208a311dc33ca837eb0
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%bcond check 1

Name:           jq
Version:        1.8.1
Release:        %autorelease
Summary:        Command-line JSON processor

License:        MIT AND ICU AND CC-BY-3.0
URL:            https://jqlang.org/
Source0:        https://github.com/jqlang/jq/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  oniguruma-devel

%ifarch %{valgrind_arches}
BuildRequires:  valgrind
%endif
BuildRequires:  make
BuildRequires:  tzdata


%description
lightweight and flexible command-line JSON processor

 jq is like sed for JSON data – you can use it to slice
 and filter and map and transform structured data with
 the same ease that sed, awk, grep and friends let you
 play with text.

 It is written in portable C, and it has zero runtime
 dependencies.

 jq can mangle the data format that you have into the
 one that you want with very little effort, and the
 program to do so is often shorter and simpler than
 you'd expect.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}


%prep
%oreon_verify_sources
%autosetup -p1

%build
# Avoid GLIBC_2.44 libm IFUNC symbols when the compose root ships an older glibc than the build host.
export CFLAGS="%{optflags} -ffp-contract=off \
-fno-builtin-exp -fno-builtin-log -fno-builtin-pow -fno-builtin-log2 -fno-builtin-exp2 \
-fno-builtin-sin -fno-builtin-cos -fno-builtin-sqrt -fno-builtin-ceil -fno-builtin-floor \
-fno-builtin-fmin -fno-builtin-fmax -fno-builtin-round -fno-builtin-trunc"
%configure --disable-static
%make_build
# Docs already shipped in jq's tarball.
# In order to build the manual page, it
# is necessary to install rake, rubygem-ronn
# and do the following steps:
#
# # yum install rake rubygem-ronn
# $ cd docs/
# $ curl -L https://get.rvm.io | bash -s stable --ruby=1.9.3
# $ source $HOME/.rvm/scripts/rvm
# $ bundle install
# $ cd ..
# $ ./configure
# $ make real_docs

%install
%make_install

%if %{with check}
%check
# Valgrind used, so restrict architectures for check
%ifarch x86_64
make check
%endif
%endif

%files
%license COPYING
%doc AUTHORS COPYING NEWS.md README.md
%{_bindir}/%{name}
%{_libdir}/libjq.so.*
%{_datadir}/man/man1/jq.1.gz

%files devel
%{_includedir}/jq.h
%{_includedir}/jv.h
%{_libdir}/libjq.so
%{_libdir}/pkgconfig/libjq.pc

%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Broaden -fno-builtin / -ffp-contract=off to avoid GLIBC_2.44 libm deps on older compose glibc

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8.1-1
- Prepare for Oreon 11 (RP1)
