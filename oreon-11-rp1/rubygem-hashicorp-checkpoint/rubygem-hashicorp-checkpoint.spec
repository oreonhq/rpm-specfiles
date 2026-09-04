%global source0_hash 928cea744b2eb0a05c7e97429e0fcb1a0ef8e0b02824271c61ff9cb2c9fe340c

# Generated from hashicorp-checkpoint-0.1.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name hashicorp-checkpoint

Name: rubygem-%{gem_name}
Version: 0.1.6
Release: 1%{?dist}
Summary: Internal HashiCorp service to check version information
License: MPL-2.0
URL: http://www.hashicorp.com
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: rubygems-devel 
# BuildRequires: rubygem(rspec) => 3.0.0
# BuildRequires: rubygem(rspec-its) => 1.0.0
BuildArch: noarch

%description
Internal HashiCorp service to check version information.

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

# Tests need internet connection
#%%check
#pushd .%%{gem_instdir}
#rspec spec
#popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/ruby-checkpoint.gemspec
%exclude %{gem_instdir}/.gitignore
%{gem_spec}
%license %{gem_instdir}/LICENSE.txt

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/Gemfile
%{gem_instdir}/spec

%changelog
%autochangelog
