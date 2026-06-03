%global source0_hash 4eeb0185c0fbfa889efed923b5b50e949cd869e7d82ac74138acd0c9c7165ec0
%global source1_hash 180f18015ce01be1d10c24e13414134363d56f9efb741fda460358bb67d96684

# Generated from ronn-ng-0.9.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ronn-ng

Name:           rubygem-%{gem_name}
Version:        0.10.1
Release:        8%{?dist}
Summary:        Builds man pages from Markdown
License:        MIT
URL:            https://github.com/apjanke/ronn-ng
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/apjanke/ronn-ng.git && cd ronn-ng
# git archive -v -o ronn-ng-0.10.1-test.tar.gz v0.10.1 test/
Source1: https://github.com/apjanke/ronn-ng/archive/refs/tags/v%{version}.tar.gz#/%{gem_name}-%{version}-test.tar.gz
# https://github.com/apjanke/ronn-ng/pull/125
# load fileutils explicitly for ruby34
Patch0:         ronn-ng-pr125-ruby34-fileutils-deps.patch
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby
BuildRequires:  rubygem(kramdown)
BuildRequires:  rubygem(kramdown-parser-gfm)
BuildRequires:  rubygem(mustache)
BuildRequires:  rubygem(nokogiri)
BuildRequires:  rubygem(test-unit)
BuildArch:      noarch

Requires:       groff-base
Provides:       rubygem-ronn = %{version}-%{release}
Obsoletes:      rubygem-ronn < 0.7.3-20

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
%setup -q -n /builddir/build/BUILD/rubygem-ronn-ng-0.10.1-build/test -b 1
(
cd %{_builddir}/test
%patch -P0 -p2
)

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Move man pages into the appropriate place
install -Dt %{buildroot}/%{_mandir}/man1/ -m 0644 %{buildroot}%{gem_instdir}/man/ronn.1
install -Dt %{buildroot}/%{_mandir}/man7/ -m 0644 %{buildroot}%{gem_instdir}/man/ronn-format.7

# Move completion scripts into the appropriate place
install -Dt %{buildroot}/usr/share/bash-completion/completions/ -m 0644 %{buildroot}%{gem_instdir}/completion/bash/ronn
install -Dt %{buildroot}/usr/share/zsh/site-functions/ -m 0644 %{buildroot}%{gem_instdir}/completion/zsh/_ronn

%check
pushd .%{gem_instdir}
cp -a %{_builddir}/test test

ruby -Itest -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{_bindir}/ronn
%{gem_instdir}/INSTALLING.md
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/bin
%exclude %{gem_instdir}/completion
%{gem_instdir}/config.ru
%{gem_libdir}
%exclude %{gem_instdir}/man
%exclude %{gem_cache}
%{gem_spec}
%{_mandir}/man1/ronn.1*
%{_mandir}/man7/ronn-format.7*
%dir %_datadir/bash-completion//
%_datadir/bash-completion/completions/
%_datadir/zsh/site-functions/

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/AUTHORS
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/ronn-ng.gemspec

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.10.1-8
- Import
