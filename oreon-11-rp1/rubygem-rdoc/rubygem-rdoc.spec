%global source1_hash 70dff3b002169a7b75c8c8ae5408e2d1b09409c9100aa4dcf8cc07ad0f442c74
%global source0_hash dfe3d0981d19b7bba71d9dbaeb57c9f4e3a7a4103162148a559c4fc687ea81f9
%global gem_name rdoc
Name: rubygem-%{gem_name}
Version: 7.0.3
Release:        1%{?dist}
Summary:        RDoc produces HTML and command-line documentation for Ruby projects
License: %{shrink:
    GPL-2.0-only AND
    Ruby AND
    BSD-3-Clause AND
    CC-BY-2.5 AND
    MIT AND
    OFL-1.1-RFN
}
URL: https://ruby.github.io/rdoc
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/ruby/rdoc/archive/refs/tags/v7.0.3.tar.gz
Patch0: rubygem-rdoc-5.1.0-ruby_version.patch
Patch1: rdoc-pr1531-fix-mutilple-document-installation.patch
Requires: rubygem(irb)
Requires: rubygem(io-console)
Requires: rubygem(json)
Provides: rdoc = %{version}-%{release}
Provides: ri = %{version}-%{release}
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(gettext)
BuildRequires:  rubygem(rake)
BuildRequires:  rubygem(test-unit-ruby-core)
BuildRequires:  rubygem(webrick)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
RDoc produces HTML and command-line documentation for Ruby projects.
RDoc includes the +rdoc+ and +ri+ tools for generating and displaying
documentation from the command-line.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -a 1
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

%patch 0 -p1
%patch 1 -p1

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
find %{buildroot}%{gem_instdir}/exe -type f | xargs chmod a+x
for n in 1; do
  mkdir -p %{buildroot}%{_mandir}/man${n}
  for file in %{buildroot}%{gem_instdir}/man/*.${n}; do
    base_name=$(basename "${file}")
    cp -a "${file}" "%{buildroot}%{_mandir}/man${n}/${base_name}"
  done
done
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

( cp -a test .%{gem_instdir}
cd .%{gem_instdir}
sed -i '/^\s*require..bundler/ s/^/#/g' test/rdoc/support/test_case.rb
RUBYOPT=-Ilib \
  ruby -e 'Dir.glob "./test/**/*_test.rb", &method(:require)' -- -v
)
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rdoc-doc -f %{oreon_filedir}/rubygem-rdoc-doc.list

%changelog

%autochangelog
