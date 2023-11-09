%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Name: kjournald
Version: 23.08.3
Release: 1
%if 0%{?git:1}
Source0:        https://invent.kde.org/system/%{name}/-/archive/master/%{name}-master.tar.bz2
%else
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
Summary: Graphical frontend for viewing the system journal
URL: https://github.com/kjournald/kjournald
License: GPL
Group: System
BuildRequires: cmake ninja
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5QmlModels)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: pkgconfig(libsystemd)

%description
Graphical frontend for viewing the system journal

%prep
%autosetup -p1
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/kjournaldbrowser
%{_libdir}/libkjournald.so*
%{_datadir}/applications/org.kde.kjournaldbrowser.desktop
%{_datadir}/metainfo/org.kde.kjournaldbrowser.appdata.xml
%{_datadir}/qlogging-categories5/kjournald.categories
