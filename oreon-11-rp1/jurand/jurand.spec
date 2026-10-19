%global source0_hash 48ecc1a45f3378e93eb55146605308a93e681e4eb2c7a17d44726ef08a5f7dd4
Name:           jurand
Version:        1.4.0
Release:        1%{?dist}
Summary:        A tool for manipulating Java symbols
License:        Apache-2.0
URL:            https://github.com/fedora-java/jurand
Source0:        https://github.com/fedora-java/jurand/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        macros.jurand
# oreon:deps
BuildRequires:  diffutils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  rubygem-asciidoctor
# /oreon:deps
%description
The tool can be used for patching .java sources in cases where using sed is
insufficient due to Java language syntax. The tool follows Java language rules
rather than applying simple regular expressions on the source code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{make_build} test-compile manpages
%install
export buildroot=%{buildroot}
export bindir=%{_bindir}
export mandir=%{_mandir}
./install.sh
install -m 644 -p -D %{SOURCE1} %{buildroot}%{_rpmmacrodir}/macros.jurand
echo "%{_rpmmacrodir}/macros.jurand" >> target/installed_files
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
