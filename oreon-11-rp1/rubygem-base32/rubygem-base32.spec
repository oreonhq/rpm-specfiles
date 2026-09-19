%global source0_hash cb9810ab7c79862ed6ead254b3a44fa2535d088396cd412eef38bdc206055aba

%global gem_name base32

Name: rubygem-%{gem_name}
Version: 0.3.4
Release: 13%{?dist}
Summary: Ruby extension for base32 encoding and decoding
License: MIT
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
%if 0%{?rhel} == 7
BuildRequires: rubygem(minitest5)
%else
BuildRequires: rubygem(minitest)
%endif
BuildArch: noarch

%description
Ruby extension for base32 encoding and decoding.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Run the test suite
%check
pushd .%{gem_instdir}
ruby -Ilib -e 'Dir.glob "./test/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE
%{gem_instdir}/config
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%license %{gem_instdir}/LICENSE
%{gem_instdir}/Rakefile
%{gem_instdir}/base32.gemspec
%{gem_instdir}/test

%changelog
%autochangelog
