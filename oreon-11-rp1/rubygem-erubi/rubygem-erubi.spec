%global source0_hash db3e3d4c9196091efcb19990c07f922b0d648902cead3fcf2bf55c9165cef489

# Generated from erubi-1.6.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name erubi

Name: rubygem-%{gem_name}
Version: 1.12.0
Release: 6%{?dist}
Summary: Small ERB Implementation
License: MIT
URL: https://github.com/jeremyevans/erubi
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/jeremyevans/erubi.git && cd erubi
# git archive -v -o erubi-1.12.0-test.tar.gz 1.12.0 test/
Source1: %{gem_name}-%{version}-test.tar.gz
# Fix compatibility with minitest 6
Patch0:  %{gem_name}-1.12.0-minitest6.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildArch: noarch

%description
Erubi is a ERB template engine for ruby. It is a simplified fork of Erubis.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1
(
cd %{_builddir}
%patch -P0 -p1
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

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/test test

ruby ./test/test.rb
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile

%changelog
%autochangelog
