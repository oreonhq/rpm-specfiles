%global source0_hash 1ee7bc55c8dcec92cf7741a2132a9a6cd19e4b884fbc1b3aca23e1a4fcd92d55
%global gem_name RedCloth
Name: rubygem-%{gem_name}
Version: 4.3.2
Release:        34%{?dist}
Summary:        Textile parser for Ruby
License: MIT
URL: http://redcloth.org
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-redcloth-4.2.9-unsigned-char-fix.patch
Patch1: rubygem-RedCloth-4.3.2-Replace-deprecated-YAML-load_documents.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Textile parser for Ruby.

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

%patch 0 -p1
%patch 1 -p1

%build

gem build %{gem_name}.gemspec
%gem_install
pushd .%{gem_instdir}/ext/redcloth_scan
mkdir ext
ln -sf .. ext/redcloth_scan
popd
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/
rm -rf %{buildroot}%{gem_instdir}/ext/
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check 

pushd .%{gem_instdir}
rspec -I$(dirs +1)%{gem_extdir_mri} spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-RedCloth-doc -f %{oreon_filedir}/rubygem-RedCloth-doc.list

%changelog

%autochangelog
