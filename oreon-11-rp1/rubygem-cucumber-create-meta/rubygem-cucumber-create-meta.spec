%global source0_hash f939306cf020b5522c390329705ea4249f54624c901e61a1fb86baaf0051dc48

# Generated from cucumber-create-meta-6.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name cucumber-create-meta

Name: rubygem-%{gem_name}
Version: 6.0.4
Release: 1%{?dist}
Summary: Produce the meta message for Cucumber Ruby
License: MIT
URL: https://github.com/cucumber/create-meta-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.3
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(sys-uname)
BuildRequires: rubygem(cucumber-messages)
BuildArch: noarch

%description
Produce the meta message for Cucumber Ruby.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%gemspec_remove_dep -g cucumber-messages "~> 17.0", ">= 17.0.1"
%gemspec_add_dep -g cucumber-messages ">= 17.0"

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
rspec spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/spec

%changelog
%autochangelog
