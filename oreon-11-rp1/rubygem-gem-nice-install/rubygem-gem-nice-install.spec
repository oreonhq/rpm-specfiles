%global source0_hash 8e825cb593dcf0222643bc74165fdbaeb6b23d28f449764f3543a19dc042b8b3
%global gem_name gem-nice-install
Name: rubygem-%{gem_name}
Version: 0.3.0
Release:        1%{?dist}
Summary:        A RubyGems plugin that improves gem installation user experience
License: MIT
URL: https://github.com/voxik/gem-nice-install
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
# /oreon:deps
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

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-gem-nice-install-doc -f %{oreon_filedir}/rubygem-gem-nice-install-doc.list

%changelog

%autochangelog
