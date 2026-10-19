%global source0_hash ec50accc911054c42398adaea9e54b42fdc68fe90686383366e77b38c692be00
%global gem_name snmp
Name:           rubygem-%{gem_name}
Version:        1.3.3
Release:        1%{?dist}
Summary:        A Ruby implementation of SNMP (the Simple Network Management Protocol)
License:        MIT
URL:            https://github.com/hallidave/ruby-snmp
VCS:            git:%{url}
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch:      noarch
%if 0%{?el7}
Provides:       rubygem(%{gem_name}) = %{version}
%endif
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
A Ruby implementation of SNMP (the Simple Network Management Protocol).

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description doc
Documentation for %{name}.

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
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if !0%{?el7}
pushd .%{gem_instdir}
ruby -Ilib -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-snmp-doc -f %{oreon_filedir}/rubygem-snmp-doc.list

%changelog

%autochangelog
