%global source0_hash 7b0c49f3e8efea77002326aaf0674d66f7c1b507cf31f7273e9931ac860a141c
%global gem_name pathspec
Name:           rubygem-%{gem_name}
Version:        0.2.1
Release:        18%{?dist}
Summary:        Use to match path patterns such as gitignore
License:        Apache-2.0
URL:            https://rubygems.org/gems/%{gem_name}
Source0:        https://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildArch:      noarch
# oreon:deps
BuildRequires:  rubygem(fakefs)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Use to match path patterns such as gitignore.

%package doc
Summary:        Documentation for %{name}
Requires:       rubygems
%description doc
Documentaion for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}
%setup -q -D -T -n %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build

gem build %{gem_name}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
mkdir -p %{buildroot}%{_bindir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
chmod 0755 %{buildroot}%{gem_instdir}/bin/pathspec-rb
mv %{buildroot}%{gem_instdir}/bin/pathspec-rb %{buildroot}%{_bindir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

echo > spec/spec_helper.rb
rspec -Ilib spec
%files -f %{oreon_filedir}/main.list
%files -n rubygem-pathspec-doc -f %{oreon_filedir}/rubygem-pathspec-doc.list

%changelog

%autochangelog
