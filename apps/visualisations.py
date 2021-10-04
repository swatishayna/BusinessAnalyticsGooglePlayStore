from src.Analyis import VisualisationAnalysis
import numpy as np
import streamlit  as st


class Analysis:
    analysis = VisualisationAnalysis()


    def run(self):
        st.title("Google Play Store Analytics\n\n\n\n")

        cleaned_data = st.checkbox("View Cleaned data")
        if cleaned_data:
            st.dataframe(self.analysis.data)


        missing_values = st.checkbox("Missing Values of the Cleaned Data")
        if missing_values:
            st.table(self.analysis.missing_values())

        data_types = st.checkbox("View Data Types of Cleaned data")
        if data_types:
            st.write(self.analysis.datatype())
            st.header("findings 1")
            st.write("Size_New, AndroidVersion_New : All the etries are numeric except 'Varies with Devices' so we will consider this as numerical columns")
            st.write("LastUpdated_New: datetime column , we will treat this later")
            st.write("14% of the data is missing in Rating Feature")
        categorical_analysis = st.checkbox("View Categorical analysis of the cleaned dataset")
        if categorical_analysis:
            st.write(self.analysis.categoricalanalysis())

        highest_installations = st.checkbox("Which category has highest number of installations")
        if highest_installations:
            st.plotly_chart(self.analysis.highestinstallations(),use_container_width=True)

        avg_category_rating =  st.checkbox("Which Category has maximum average rating")
        if avg_category_rating:
            st.plotly_chart(self.analysis.avg_CategoryRating()[0],use_container_width=True)
            st.header("Findings")
            st.write(
                """top 12 categories in terms rating include categories which has least number of installations except Games and Social,
                categories with extremely low number of installations cant be compared with categories with extremely high installation in terms of ratings
                we will check the average ratings of top 10 categories n terms of installations
                Game and Social categories are very much popular and favourable by the ppl""")
            st.plotly_chart(self.analysis.avg_CategoryRating()[1], use_container_width=True)
            st.header("Findings")
            st.write(
                """it seems like Game Category is performing good in terms of number of installations and rating followed by social
                 \nTools catgeory has the lowest rating among top installed categories, better apps in this category can be launched or the existing app can be looked upon for further improvements""")

        max_reviews =  st.checkbox("Which Category has maximum number of reviews submitted on GPS")
        if max_reviews:
            st.plotly_chart(self.analysis.max_reviews(),use_container_width=True)
            st.header("Findings")
            st.write(
                """It seems like Family category apps have maximum reviews submitted, thtere could be many reasons for it one reason could be family is an integral part and ppl dont want to miss reporting any good/bad reviews on it so that others can consider those points
                Since Game category has maximum number of installation it was expected to have good amount of reveiws
                Events and last few categories have least number of reviews submitted which is obvious as users ar less in number for these categories""")

        highestinstalled_highestreviews = st.checkbox("Which of the highest Installed category has highest ratings submitted?")
        if highestinstalled_highestreviews:
            st.plotly_chart(self.analysis.highestinstalled_highestreviews(),use_container_width=True)
            st.header("Findings")
            st.write("""Though the number of installation in Game category is highest but in terms of review collection it is very low.
                \nWe can include a scheme wherein the user can have extra lives in the game if he submits review on the google play store or may be extension of trial. The reviews can then be used for improvements.
                \nThe Benefits of Reviews for the Google Play Store as per https://www.makeuseof.com/why-you-should-leave-reviews-on-the-google-play-store/
                \nLeaving reviews for an app not only helps the users and the developers, but also the Google Play Store itself. The Play Store's goal as an app platform is to show you fast, accurate, and personalized results when you search for your desired app and keep spam apps away.
                To make that happen, it needs information on the app's performance—which is displayed via user reviews. An app that has a 4.5-star rating is most probably safer and more relevant than an app with a 2-star rating of the same genre.
                \nThis information helps Google's algorithm better rank the apps on the Play Store and bring you high-quality app results that you are most likely to download and have a good experience with. The more favorable an app's rating and reviews, 
                the more the number of people downloading that app and using Play Store's services.""")

        paid_categories = st.checkbox("Which categories are of Type paid")
        if paid_categories:
            st.plotly_chart(self.analysis.paid_categories(), use_container_width=True)

        highest_paid_installed = st.checkbox("which are the categories with highest number of paid installations?")
        if highest_paid_installed:
            st.plotly_chart(self.analysis.highest_paid_installed(), use_container_width=True)
            st.header("Findings")
            st.write(
                """Paid apps from Family category are installed maximum though in overall installations (paid+free) Game Category is at top with 35Billion + installations and Family at 6 Place with 10 Billion+ Installations
                \nThere could be many reasons for this. One reason seems like app could be providing one to one consultation to the person which is more preferred over a generalised app which are mostly free""")

        paid_highestrating = st.checkbox("Which category with paid apps has highest ratings?")
        if paid_highestrating:
            st.plotly_chart(self.analysis.paid_highestrating(), use_container_width=True)
            st.header("Findings")
            st.write("""
                The average rating of paid News And Magzines is highest howsoever Games which has highest number of installations and family with hihgest number of pai dinstallatons needs improvement
                \nBetter Family apps can be of great scope
                \nPaid parenting app has least average rating , This is the category which needs alot of improvement. Total Installations of Parenting Category Apps is 25K+ which is very less""")

        highestReviews_paid = st.checkbox("Which category has highest number of Reviews submitted for paid apps?")
        if highestReviews_paid:
            st.plotly_chart(self.analysis.highestReviews_paid(), use_container_width=True)
        contentrating_highestinstall = st.checkbox("Which ContentRating has highest number of Installations?")
        if contentrating_highestinstall:
            st.plotly_chart(self.analysis.contentrating_highestinstall(), use_container_width=True)

        size_apps = st.checkbox("Categories with number of app w.r.t size")
        if size_apps:
            min_size = int(np.round(self.analysis.temp_df()[0]))
            max_size = int(np.round(self.analysis.temp_df()[1]))

            x = st.slider('Size', max_value=max_size, min_value=min_size) # 👈 this is a widget
            if x:
                st.write("Number of applications in each category where the size of the application is greater than", x)
                st.plotly_chart(self.analysis.size_apps(x), use_container_width=True)
                st.header("Findings")
                st.write(
                "Family apps and games categories have heavy apps which is very obvious")