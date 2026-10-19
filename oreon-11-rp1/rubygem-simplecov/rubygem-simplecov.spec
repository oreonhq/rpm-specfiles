%global source0_hash c78227427eb6b40499d657f2996ec6841f5135468693e55e3d2c976c706f86e4
%global gem_name simplecov
%global rubyabi 1.9.1
Summary:        Code coverage analysis tool for Ruby 1.9
Name:          rubygem-%{gem_name}
Version:       0.13.0
Release:        1%{?dist}
License:       MIT
URL:           http://github.com/colszowka/simplecov
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?fedora} >= 19 || 0%{?rhel} > 6 || 0%{?oreon} >= 11
Requires:      ruby(release)
%else
Requires:      ruby(abi) >= %{rubyabi}
%endif
Requires:      ruby 
Requires:      rubygems
Requires:      rubygem(docile) => 1.1.0
Requires:      rubygem(multi_json) => 1.0
Requires:      rubygem(simplecov-html) => 0.8.0
BuildArch:     noarch
Provides:      rubygem(%{gem_name}) = %{version}
# oreon:deps
BuildRequires:  ruby
BuildRequires:  rubygem(aruba)
BuildRequires:  rubygem(bundler)
BuildRequires:  rubygem(capybara)
BuildRequires:  rubygem(cucumber)
BuildRequires:  rubygem(docile)
BuildRequires:  rubygem(rake)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(simplecov-html)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Code coverage for Ruby 1.9 with a powerful configuration library and automatic
merging of coverage across test suites

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build

gem build %{gem_name}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
rm -f %{buildroot}%{gem_instdir}/.gitignore
rm -f %{buildroot}%{gem_instdir}/.rspec
rm -f %{buildroot}%{gem_instdir}/.rubocop.yml
rm -f %{buildroot}%{gem_instdir}/.travis.yml
rm -rf %{buildroot}%{gem_instdir}/.yardopts
rm -rf %{buildroot}%{gem_instdir}/.yardoc
rm -f %{buildroot}%{gem_instdir}/Gemfile
rm -f %{buildroot}%{gem_instdir}/simplecov.gemspec
chmod 0755 %{buildroot}%{gem_instdir}/Rakefile
mv %{buildroot}%{gem_instdir}/doc %{buildroot}/%{gem_docdir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd %{buildroot}%{gem_instdir}
rm -rf spec/faked_project/
rspec -Ilib spec
rm -rf %{buildroot}%{gem_instdir}/tmp
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-simplecov-doc -f %{oreon_filedir}/rubygem-simplecov-doc.list

%changelog

%autochangelog
