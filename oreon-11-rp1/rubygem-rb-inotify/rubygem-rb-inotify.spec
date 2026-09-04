%global source0_hash a0a700441239b0ff18eb65e3866236cd78613d6b9f78fea1f9ac47a85e47be6e

%global gem_name rb-inotify

Name: rubygem-%{gem_name}
Version: 0.11.1
Release: 1%{?dist}
Summary: A Ruby wrapper for Linux inotify, using FFI
License: MIT
URL: https://github.com/guard/rb-inotify
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(ffi)
BuildRequires: %{_bindir}/rspec
BuildRequires: rubygem(concurrent-ruby)
BuildRequires: rubygem(rspec-expectations)
BuildArch: noarch

%description
A Ruby wrapper for Linux inotify, using FFI.

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
# Bundler is not necessary.
sed -i "/bundler\/setup/ s/^/#/" spec/spec_helper.rb

# Bunler needs "Pathname" for its functionality, but we are not using Bundler,
# therefore we need to load it explicitly.
rspec -rpathname spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/rb-inotify.gemspec
%{gem_instdir}/spec

%changelog
%autochangelog
