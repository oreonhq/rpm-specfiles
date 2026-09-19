%global source0_hash 5d83c0822d1aaea32a278a99b1afedd3f28e14cfff846e96987bb24ebcb3fd45

# Generated from rails-1.2.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rails

Name: rubygem-%{gem_name}
Epoch: 1
Version: 8.0.3
Release: 2%{?dist}
Summary: Full-stack web application framework
License: MIT
URL: https://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}%{?prerelease}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.8.11
BuildRequires: ruby >= 3.2.0
BuildArch: noarch

%description
Ruby on Rails is a full-stack web framework optimized for programmer happiness
and sustainable productivity. It encourages beautiful code by favoring
convention over configuration.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}%{?prerelease}

%build
gem build ../%{gem_name}-%{version}%{?prerelease}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
