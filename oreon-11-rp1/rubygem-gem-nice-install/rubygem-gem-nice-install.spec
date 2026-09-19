%global source0_hash 8e825cb593dcf0222643bc74165fdbaeb6b23d28f449764f3543a19dc042b8b3

# Generated from gem-nice-install-0.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name gem-nice-install

Name: rubygem-%{gem_name}
Version: 0.3.0
Release: 23%{?dist}
Summary: A RubyGems plugin that improves gem installation user experience
License: MIT
URL: https://github.com/voxik/gem-nice-install
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch

%description
A RubyGems plugin that improves gem installation user experience. If binary
extension build fails, it tries to install its development dependencies.

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
# No upstream test suite :(
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT
%{gem_instdir}/data
%{gem_libdir}
%exclude %{gem_cache}
%{gem_plugin}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
