%global source0_hash 8c7f690002ea22c139f3a64394aef2e816e00ca47fd971af7d54a66087356dd2

# Force out of source build
%undefine __cmake_in_source_build

# base pkg default to SQLITE now, install -mysql if you want that instead
%global database_backend SQLITE

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

Summary: PIM Storage Service Libraries
Name:    akonadi
Version: 1.13.0
Release: 131%{?dist}

License: LGPL-2.0-or-later
URL:     http://community.kde.org/KDE_PIM/Akonadi 
Source0: http://download.kde.org/stable/akonadi/src/akonadi-%{version}.tar.bz2

## downstream patches
Patch100: akonadi-1.13.0-libs_only.patch

## upstreamable patches

## upstream patches (1.13 branch)
Patch1: 0001-FindSqlite-Use-CMAKE_FLAGS-the-right-way-in-try_comp.patch
Patch2: 0002-Do-not-enter-the-test-directories-if-AKONADI_BUILD_T.patch
Patch3: 0003-STORE-Allow-modifying-items-tags-via-Tag-RID-or-GID.patch
Patch4: 0004-Fix-typo-in-if-condition.patch
Patch5: 0005-Fix-buffer-overflow-in-AKTEST_FAKESERVER_MAIN.patch
Patch6: 0006-Don-t-crash-when-setmntent-returns-NULL.patch
Patch7: 0007-Don-t-call-insert-from-Q_ASSERT-breaks-unit-tests-in.patch
Patch8: 0008-Suppress-unused-variable-warnings-in-release-mode.patch
Patch9: 0009-Test-whether-compiler-supports-all-required-C-11-fea.patch
Patch10: 0010-prevent-starting-a-QTimer-with-a-negative-interval.patch
Patch11: 0011-Convert-some-qDebugs-to-akDebugs.patch
Patch12: 0012-Optimize-Reduce-the-amount-of-allocations-required-t.patch
Patch13: 0013-Intern-entity-strings-for-table-and-column-names.patch
Patch14: 0014-No-semicolon-after-Q_DECLARE_METATYPE.patch
Patch15: 0015-Use-QMutexLocker-instead-of-manual-lock-unlock-calls.patch
Patch16: 0016-Use-an-QAtomicInt-instead-of-a-plain-bool-for-Entity.patch
Patch17: 0017-Optimize-Only-do-one-hash-lookup-to-retrieve-value-f.patch
Patch18: 0018-Optimize-Skip-value-condition-on-invalid-flags.patch
Patch19: 0019-Optimize-queries-Do-not-retrieve-known-key-used-in-t.patch
Patch20: 0020-Avoid-ridiculous-amount-of-SQL-queries-by-caching-Pa.patch
Patch21: 0021-Implement-support-for-CASE.WHEN.THEN-SQL-statements-.patch
Patch22: 0022-Implement-cache-for-CollectionStatistics-to-signific.patch
Patch23: 0023-Always-create-a-new-PartType-when-it-does-not-exist.patch
Patch24: 0024-Fix-compilation-with-strict-iterators.patch
Patch25: 0025-Avoid-repeated-calls-to-PimItem-flags-and-PimItem-ta.patch
Patch26: 0026-Avoid-recursive-collection-listing-in-SearchHelper.patch
Patch27: 0027-Minor-improvements-in-StatisticsCache-as-suggested-b.patch
Patch28: 0028-Extend-imapparser-benchmark-and-keep-static-data-aro.patch
Patch29: 0029-Reduce-the-amount-of-allocations-by-preallocating-a-.patch
Patch30: 0030-Preallocate-a-capacity-of-16-for-the-returned-list.patch

BuildRequires: automoc4
BuildRequires: boost-devel
BuildRequires: cmake >= 2.8.8
BuildRequires: gcc-c++
# for xsltproc
BuildRequires: libxslt
BuildRequires: pkgconfig(QtDBus) pkgconfig(QtSql) pkgconfig(QtXml)
BuildRequires: pkgconfig(shared-mime-info)

%description
%{summary}.

%package devel
Summary: Developer files for %{name}
Conflicts: kf5-akonadi-server-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n akonadi-%{version}

%build
%cmake -DCMAKE_BUILD_TYPE:STRING="Release"
%cmake_build

%install
%cmake_install

## unpackaged files
rm -fv %{buildroot}%{_datadir}/mime/packages/akonadi-mime.xml

%check
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion akonadi)" = "%{version}"

%ldconfig_scriptlets

%files
%doc AUTHORS
%license lgpl-license
%{_libdir}/libakonadiprotocolinternals.so.1*

%files devel
%{_includedir}/akonadi/
%{_libdir}/pkgconfig/akonadi.pc
%{_libdir}/libakonadiprotocolinternals.so
%{_libdir}/cmake/Akonadi/
%{_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.*.xml

%changelog
%autochangelog
