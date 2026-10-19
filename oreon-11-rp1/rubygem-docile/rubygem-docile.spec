%global source0_hash 5d3ee40b3a6567fe460601f3f4a3e199a98de37434ebfa242d751d0c79181255
%global gem_name docile
Summary:        Docile keeps your Ruby DSLs tame and well-behaved
Name:          rubygem-%{gem_name}
Version:       1.1.5
Release:        1%{?dist}
License:       MIT
URL:           https://ms-ati.github.com/docile/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:        docile-pr106-ruby33-NomethodError-msg.patch
Patch1:        docile-pr108-support-ruby34-error-msg-syntax.patch
%if 0%{?fc19} || 0%{?fc20} || 0%{?el7}
Requires:      ruby(release)
Requires:      ruby(rubygems)
%endif
BuildArch:     noarch
%if 0%{?fc19} || 0%{?fc20} || 0%{?el7}
Provides:      rubygem(%{gem_name}) = %{version}
%endif
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(mime-types)
BuildRequires:  rubygem(rake)
BuildRequires:  rubygem(redcarpet)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(yard)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Docile turns any Ruby object into a DSL.
Especially useful with the Builder pattern.

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
%patch -P0 -p1
%patch -P1 -p1
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build

gem build %{gem_name}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
rm -rf %{buildroot}%{gem_instdir}/{.coveralls.yml,.gitignore,.rspec,.ruby-gemset,.ruby-version,.travis.yml,.yard*}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

rspec -Ilib spec
%files -f %{oreon_filedir}/main.list
%files -n rubygem-docile-doc -f %{oreon_filedir}/rubygem-docile-doc.list

%changelog

%autochangelog
