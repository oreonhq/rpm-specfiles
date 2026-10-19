%global source0_hash 4eeb0185c0fbfa889efed923b5b50e949cd869e7d82ac74138acd0c9c7165ec0
%global source1_hash 180f18015ce01be1d10c24e13414134363d56f9efb741fda460358bb67d96684
%global gem_name ronn-ng
Name:           rubygem-%{gem_name}
Version:        0.10.1
Release:        8%{?dist}
Summary:        Builds man pages from Markdown
License:        MIT
URL:            https://github.com/apjanke/ronn-ng
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/apjanke/ronn-ng/archive/refs/tags/v%{version}.tar.gz#/%{gem_name}-%{version}-test.tar.gz
Patch0:         ronn-ng-pr125-ruby34-fileutils-deps.patch
BuildArch:      noarch
Requires:       groff-base
Provides:       rubygem-ronn = %{version}-%{release}
Obsoletes:      rubygem-ronn < 0.7.3-20
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(kramdown)
BuildRequires:  rubygem(kramdown-parser-gfm)
BuildRequires:  rubygem(mustache)
BuildRequires:  rubygem(nokogiri)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Ronn-NG builds manuals in HTML and Unix man page format from Markdown.

The source format includes all of Markdown but has a more rigid structure and
syntax extensions for features commonly found in man pages (definition lists,
link notation, etc.). The ronn-format(7) manual page defines the format in
detail.

%package doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{gem_name}-%{version} -b 1
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;
(
cd test
%patch -P0 -p2
)

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
install -Dt %{buildroot}/%{_mandir}/man1/ -m 0644 %{buildroot}%{gem_instdir}/man/ronn.1
install -Dt %{buildroot}/%{_mandir}/man7/ -m 0644 %{buildroot}%{gem_instdir}/man/ronn-format.7
install -Dt %{buildroot}/usr/share/bash-completion/completions/ -m 0644 %{buildroot}%{gem_instdir}/completion/bash/ronn
install -Dt %{buildroot}/usr/share/zsh/site-functions/ -m 0644 %{buildroot}%{gem_instdir}/completion/zsh/_ronn
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
cp -a %{_builddir}/%{gem_name}-%{version}/test test
ruby -Itest -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-ronn-ng-doc -f %{oreon_filedir}/rubygem-ronn-ng-doc.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.10.1-8
- Import
