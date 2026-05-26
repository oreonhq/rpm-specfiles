Name:           jurand
Version:        1.3.5
Release:        %autorelease
Summary:        A tool for manipulating Java symbols
License:        Apache-2.0
URL:            https://github.com/fedora-java/jurand

Source0:        https://github.com/fedora-java/jurand/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 e8e01cf13b08dfd9c8c60367bcb172c0dd09a161a7c2a351c08cfba246d64d4a
%global source0_file 1.3.5.tar.gz
# oreon url source checksums end

BuildRequires:  diffutils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  rubygem-asciidoctor

%description
The tool can be used for patching .java sources in cases where using sed is
insufficient due to Java language syntax. The tool follows Java language rules
rather than applying simple regular expressions on the source code.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/1.3.5.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "e8e01cf13b08dfd9c8c60367bcb172c0dd09a161a7c2a351c08cfba246d64d4a" || { echo "oreon: Source0 SHA256 mismatch for 1.3.5.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -C

%build
%{make_build} test-compile manpages

%install
export buildroot=%{buildroot}
export bindir=%{_bindir}
export rpmmacrodir=%{_rpmmacrodir}
export mandir=%{_mandir}

./install.sh

%check
make test

%files -f target/installed_files
%dir %{_rpmconfigdir}
%dir %{_rpmmacrodir}
%license LICENSE NOTICE
%doc README.adoc

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.5-1
- Import
