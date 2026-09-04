%global source0_hash 59805315dcc392a76b358978cb3007dd140b9500e984986b1588837d986d11f9

# Generated from ammeter-0.2.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ammeter

Name: rubygem-%{gem_name}
Version: 1.1.7
Release: 1%{?dist}
Summary: Write specs for your Rails 3+ generators
License: MIT
URL: https://github.com/alexrothenberg/%{gem_name}
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(activerecord)
BuildRequires: rubygem(haml)
BuildRequires: rubygem(railties)
BuildRequires: rubygem(rspec-rails) >= 2.2
BuildRequires: rubygem(sqlite3)
BuildArch: noarch

%description
Write specs for your Rails 3+ generators.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# Fix test suite for Ruby 2.3 compatibility.
# File#read is re-defined in spec/spec_helpr.rb#stub_file,
# and File#read is also used in 'require': specification.rb#load.
# If the first "require" for on library is called after the stub definition,
# it is failed.
rspec -r haml spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/History.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/ammeter.gemspec
%{gem_instdir}/features
%{gem_instdir}/spec

%changelog
%autochangelog
